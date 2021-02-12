from wordcloud import WordCloud, STOPWORDS
import imageio
import matplotlib.pyplot as plt
from collections import Counter


def random_red_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None,
                          random_state=None):
    h = 0
    s = 100
    l = int(50 * (float(random_state.randint(60, 120)) / 100.0))
    return "hsl({}, {}%, {}%)".format(h, s, l)


def generate_word_cloud(words, image_file, saved_name):
    mask = imageio.imread(image_file)
    word_cloud = WordCloud(width=400,
                           height=400,
                           color_func=random_red_color_func,
                           background_color='white',
                           stopwords=STOPWORDS,
                           mask=mask).generate_from_frequencies(words)
    plt.figure(figsize=(10, 8), facecolor='white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(saved_name)


myLove = ['Juliann and Zach', 'Love', 'Eternity', 'Mexico', 'Church', 'Family', 'Happiness', 'Amor', 'Familia', 'Life', 'Hawaii', ' \
         ''Music', 'New York', 'Te Amo', 'Build A Mansion', 'Beauty', 'Grace', 'Aila', '']

word_cloud_dict = Counter(myLove)

generate_word_cloud(word_cloud_dict, '../Desktop/temple.png', '_word_cloud.png')

