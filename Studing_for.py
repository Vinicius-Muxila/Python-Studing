{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPtid9qLtwTTgIhIuds5wHJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Vinicius-Muxila/Python-Studing/blob/main/Studing_for.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bDxY8--8JkKR",
        "outputId": "5c3c5bf5-6e12-4508-c77b-b7ad0b123188"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n",
            "Digite um número que queira multiplicar: 3\n",
            "3 x 1 = 3\n",
            "3 x 2 = 6\n",
            "3 x 3 = 9\n",
            "3 x 4 = 12\n",
            "3 x 5 = 15\n",
            "3 x 6 = 18\n",
            "3 x 7 = 21\n",
            "3 x 8 = 24\n",
            "3 x 9 = 27\n",
            "3 x 10 = 30\n",
            "\n",
            "Digite um número que queira dividir: 10\n",
            "10.0 / 1 = 10.00\n",
            "10.0 / 2 = 5.00\n",
            "10.0 / 3 = 3.33\n",
            "10.0 / 4 = 2.50\n",
            "10.0 / 5 = 2.00\n",
            "10.0 / 6 = 1.67\n",
            "10.0 / 7 = 1.43\n",
            "10.0 / 8 = 1.25\n",
            "10.0 / 9 = 1.11\n",
            "10.0 / 10 = 1.00\n"
          ]
        }
      ],
      "source": [
        "# Exercício 1 — Contador Simples\n",
        "# Escreva um programa que exiba os números de 1 a 10, um por linha.\n",
        "\n",
        "for i in range(1,11):\n",
        "  print(i)\n",
        "\n",
        "# Exercício 2 — Tabuada\n",
        "# Peça para o usuário digitar um número inteiro, e exiba a tabuada desse número de 1 a 10.\n",
        "\n",
        "numero = int(input(\"Digite um número que queira multiplicar: \"))\n",
        "inicio = 0\n",
        "for inicio in range(1,11):\n",
        "  resultado = inicio * numero\n",
        "  print(numero, \"x\", inicio, \"=\", resultado)\n",
        "\n",
        "numero = float(input(\"\\nDigite um número que queira dividir: \"))\n",
        "inicio = 0\n",
        "for inicio in range(1,11):\n",
        "  resultado = numero / inicio\n",
        "  print(numero, \"/\", inicio, \"=\", f\"{resultado:.2f}\")"
      ]
    }
  ]
}