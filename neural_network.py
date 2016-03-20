# -*- coding: utf-8 -*-

import numpy as np
import _pickle as pickle #Python 3
# import cPickle as pickle #Python 2
import os


class NeuralNetwork:
    def __init__(self):
        np.seterr(divide='raise', over='raise', invalid='ignore')

        try:
            WEIGHTS_PATH = os.getcwd()+"/Weights/"
            letter_weight = os.path.join(WEIGHTS_PATH, "letters_nn.wt")
            number_weight = os.path.join(WEIGHTS_PATH, "numbers_nn.wt")

            is_letter_weight = os.path.exists(letter_weight)
            is_number_weight = os.path.exists(number_weight)

            if is_letter_weight and is_number_weight:
                letter_file = open(letter_weight, "rb")
                number_file = open(number_weight, "rb")

            else:
                raise IOError

            self.letter_weights = pickle.load(letter_file, encoding='latin1')
            self.number_weights = pickle.load(number_file, encoding='latin1')
            
        except Exception as e:
            raise e

    def add_biasnode(self, output):
        temp_out = output.tolist()
        temp_out.append([1])
        output = np.array(temp_out)
        return output

    def remove_biasnode(self, output):
        temp_out = output.copy().tolist()
        temp_out.pop()
        output = np.array(temp_out)
        return output

    def sigmoid(self, num_x):
        return 1 / (1 + np.exp(-num_x))

    def softmax(self, out_O):
        return np.exp(out_O) / np.sum(np.exp(out_O))

    def forward(self, input_data, character_set):
        if character_set == 0:
            input_to_hidden = self.letter_weights[0]
            hidden_to_output = self.letter_weights[1]
            ascii_value = 65

        elif character_set == 1:
            input_to_hidden = self.number_weights[0]
            hidden_to_output = self.number_weights[1]
            ascii_value = 48

        in_I = input_data
        out_I = in_I

        in_H = np.dot(input_to_hidden.T, self.add_biasnode(out_I))
        out_H = self.sigmoid(in_H)

        in_O = np.dot(hidden_to_output.T, self.add_biasnode(out_H))
        out_O = self.softmax(in_O)
        return chr(ascii_value + np.argmax(out_O))

    def compute_character(self, picture, state):
        data = np.ravel(picture).reshape(picture.size, 1)
        character = self.forward(data, state)
        return character


def main():
    neural_net = NeuralNetwork()

if __name__ == '__main__':
	main()