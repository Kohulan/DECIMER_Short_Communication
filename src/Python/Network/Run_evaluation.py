import tensorflow as tf
import os
import sys
import pickle
import I2S_Model_Transformer
import selfies
import numpy as np
import argparse
import efficientnet.tfkeras as efn

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='+')

args = parser.parse_args()

os.environ["CUDA_VISIBLE_DEVICES"]="0"
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
print(args)
for file_in in args.file:
	f = open('Preds_'+str(file_in)+'.txt' , 'w')
	sys.stdout = f
	tokenizer = pickle.load(open("tokenizer_Isomeric_SMILES.pkl","rb"))
	maxlength = pickle.load(open("max_length_Isomeric_SMILES.pkl","rb"))

	target_vocab_size = len(tokenizer.word_index)
	num_layer = 4
	d_model = 512
	dff = 2048
	num_heads = 8
	row_size = 10
	col_size = 10
	dropout_rate = 0.1

	optimizer = tf.keras.optimizers.Adam(learning_rate=0.00051)

	transformer = I2S_Model_Transformer.Transformer(num_layer,d_model,num_heads,dff,row_size,col_size,target_vocab_size,max_pos_encoding=target_vocab_size,rate=dropout_rate)
	target_size=(300,300,3)
	def load_image(image_path):
		img = tf.io.read_file(image_path)
		img = tf.image.decode_png(img, channels=3)
		img = tf.image.resize(img, (300, 300))
		img = efn.preprocess_input(img)
		return img, image_path

	#Using EfficientnetB3 and using the pretrained Imagenet weights
	image_model = efn.EfficientNetB3(weights='noisy-student',input_shape=target_size, include_top=False)

	new_input = image_model.input
	hidden_layer = image_model.layers[-1].output

	image_features_extract_model = tf.keras.Model(new_input, hidden_layer)
	def create_padding_mask(seq):
		seq = tf.cast(tf.math.equal(seq, 0), tf.float32)
		
		# add extra dimensions to add the padding
		# to the attention logits.
		return seq[:, tf.newaxis, tf.newaxis, :] # (batch_size, 1, 1, seq_len)

	def create_look_ahead_mask(size):
		mask = 1 - tf.linalg.band_part(tf.ones((size, size)), -1, 0)
		return mask  # (seq_len, seq_len)

	def create_masks_decoder(tar):
		look_ahead_mask = create_look_ahead_mask(tf.shape(tar)[1])
		dec_target_padding_mask = create_padding_mask(tar)
		combined_mask = tf.maximum(dec_target_padding_mask, look_ahead_mask)
		return combined_mask

	#Evaluator
	def evaluate(image):
		temp_input = tf.expand_dims(load_image(image)[0], 0)
		img_tensor_val = image_features_extract_model(temp_input)
		img_tensor_val = tf.reshape(img_tensor_val, (img_tensor_val.shape[0], -1, img_tensor_val.shape[3]))

		output = tf.expand_dims([tokenizer.word_index['<start>']], 0)
		result = []
		end_token = tokenizer.word_index['<end>']

		for i in range(maxlength):
			dec_mask = create_masks_decoder(output)

			predictions, attention_weights = transformer(img_tensor_val,output,False,dec_mask)
			predictions = predictions[: ,-1:, :]  # (batch_size, 1, vocab_size)
			predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)

			if predicted_id == end_token:
				return result#,tf.squeeze(output, axis=0), attention_weights

			result.append(tokenizer.index_word[int(predicted_id)])
			output = tf.concat([output, predicted_id], axis=-1)

		return result#,tf.squeeze(output, axis=0), attention_weights

	checkpoint_path = "SMILES"
	ckpt = tf.train.Checkpoint(transformer=transformer,optimizer=optimizer)
	ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=50)

	if ckpt_manager.latest_checkpoint:
		ckpt.restore(tf.train.latest_checkpoint(checkpoint_path))

	# Predicting Smiles on the validation set
	with open(str(file_in), 'r') as txt_file:
		for i,line in enumerate(txt_file):
			img = line.strip().split("\t")[0]
			cap = line.strip().split("\t")[1]
			image = 'PubChem_images/'+img+'.png'
			real_caption = ''.join(cap)
			result = evaluate(image)

			print (real_caption.replace(" ","").replace("<start>","").replace("<end>",""),'\tOriginalSmiles', flush=True)
			print (''.join(result).replace("<start>","").replace("<end>",""),'\tPredictedSmiles', flush=True)
	#print("Predictions Completed!")
f.close()