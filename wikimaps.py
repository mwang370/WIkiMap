import wikipedia
import random
import matplotlib.pyplot as plt
import matplotlib.font_manager as ft
import seaborn as sns
import numpy as np

def drawGraph(topic, links):
    sns.set_style('dark')
    x_coord = []
    y_coord = []
    angles = []
    angle = 0
    for x in range(10):
        x_coord.append(10 * np.cos(angle))
        y_coord.append(10 * np.sin(angle))
        angles.append(angle)
        angle = angle + np.pi/5

    fig = plt.figure(figsize = (15, 15))
    ax = fig.add_subplot(1, 1, 1)
    
    ax.scatter(0, 0, s= 12000, alpha = 1, c= "lightgray", zorder = 3)
    ax.scatter(x_coord, y_coord, s = 8000, c= angles, alpha=1, zorder = 3, cmap=plt.cm.RdYlGn)

    for x in range(10):
        ax.plot([0, x_coord[x]], [0, y_coord[x]], 'w--', zorder = 1)

    ax.text(0,0-2.7, topic, fontsize = 20)
    ax.text(-1,-0.2, "HOME", fontsize = 20)
    for x in range(10):
        ax.text(x_coord[x],y_coord[x]-2.4,links[x], fontsize = 20)
        ax.text(x_coord[x]-0.2, y_coord[x]-0.2, x, fontsize = 20)


    plt.xticks([])
    plt.yticks([])

    plt.show()


def search():
    topic = input("What do you want to learn about? ")
    try:
        topic = wikipedia.search(topic)[0]
        return topic, wikipedia.page(topic)
    except:
        print("Hey, sorry, we couldn't find anything. Try again.")
        return search()

def retrieveLinks(page):
    linkslist = page.links
    for i in linkslist:
        if len(i) > 15:
            linkslist.remove(i)
            
    ten_links = [linkslist[x] for x in random.sample(range(0, len(linkslist)), 10)]
    
    return ten_links

def displaySummary(topic):
    print(wikipedia.summary(topic, sentences=5))

def main():
    topic, page = search()
    linksToDisplay = retrieveLinks(page)
    drawGraph(topic, linksToDisplay)
    
    while True:
        userInput = input("Next? (Type 's' for summary, 't' for full text, and 'n' for new search) ")
        if userInput == 's':
            displaySummary(topic)
        elif userInput == 'n':
            main()
        elif userInput == 't':
            print(page.content)
        elif userInput == 'q':
            break
        else:
            nex = int(userInput)
            topic = wikipedia.search(linksToDisplay[nex])[0]
            page = wikipedia.page(topic)
            linksToDisplay = retrieveLinks(page)
            drawGraph(topic, linksToDisplay)

main()
