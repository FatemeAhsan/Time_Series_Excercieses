{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyN7+eQqOyD3Iy62Ue28J4XZ"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Install Packages"
      ],
      "metadata": {
        "id": "XAOwIbWnAgZC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install github-clone"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gKvWj418AQtA",
        "outputId": "396d31f0-0c97-4c2f-8887-9355431dbfcb"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting github-clone\n",
            "  Downloading github_clone-1.2.0-py3-none-any.whl (9.1 kB)\n",
            "Requirement already satisfied: requests>=2.20.0 in /usr/local/lib/python3.10/dist-packages (from github-clone) (2.31.0)\n",
            "Collecting docopt>=0.6.2 (from github-clone)\n",
            "  Downloading docopt-0.6.2.tar.gz (25 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20.0->github-clone) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20.0->github-clone) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20.0->github-clone) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20.0->github-clone) (2023.7.22)\n",
            "Building wheels for collected packages: docopt\n",
            "  Building wheel for docopt (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for docopt: filename=docopt-0.6.2-py2.py3-none-any.whl size=13706 sha256=27a64d2a719622d4bce33e78b66dd247bb7fc68c8ed624425a50aa4b05be1298\n",
            "  Stored in directory: /root/.cache/pip/wheels/fc/ab/d4/5da2067ac95b36618c629a5f93f809425700506f72c9732fac\n",
            "Successfully built docopt\n",
            "Installing collected packages: docopt, github-clone\n",
            "Successfully installed docopt-0.6.2 github-clone-1.2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Load Utils"
      ],
      "metadata": {
        "id": "Ej9IEI0HAnqI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!ghclone https://github.com/FatemehAhsan/AI_Practices/tree/main/utils"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jAv4wpl6ApO-",
        "outputId": "6f396f54-c993-4db2-f6a9-46debfed1f04"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'utils'...\n",
            "done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Import Modules"
      ],
      "metadata": {
        "id": "TrpbMYFeAzc2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from utils import utils"
      ],
      "metadata": {
        "id": "GIGGpZRqAx62"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Train"
      ],
      "metadata": {
        "id": "lgJg5SE4BO2Q"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "utils.set_kaggle_api()"
      ],
      "metadata": {
        "id": "N4901wTo8LRw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EFg0BTwM6sJH",
        "outputId": "2553dc3d-5720-47cf-c251-41ae9e7f0743"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading cifar-10.zip to /content\n",
            " 97% 693M/715M [00:03<00:00, 273MB/s]\n",
            "100% 715M/715M [00:03<00:00, 219MB/s]\n"
          ]
        }
      ],
      "source": [
        "utils.download_kaggle_competition('cifar-10')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "utils.unzip('cifar-10.zip')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FMhlvyj8AFLZ",
        "outputId": "c033f4c9-53ff-4b73-953a-6db39f524c41"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archive:  cifar-10.zip\n",
            "  inflating: sampleSubmission.csv    \n",
            "  inflating: test.7z                 \n",
            "  inflating: train.7z                \n",
            "  inflating: trainLabels.csv         \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "labels = utils.read_csv_labels('trainLabels.csv')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 176
        },
        "id": "RRJQbxD_CAj9",
        "outputId": "1f7caf50-cd1d-4f02-a1c9-c6a2b5a4b010"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "error",
          "ename": "AttributeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-22-88c0771f7c71>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mlabels\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv_labels\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'trainLabels.csv'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m: module 'utils.utils' has no attribute 'read_csv_labels'"
          ]
        }
      ]
    }
  ]
}