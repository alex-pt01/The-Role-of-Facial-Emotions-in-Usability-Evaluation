import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import itertools

def show_train_test_distribution(test_count,train_count,MODEL_NAME,DATASET_NAME):
        # # lot distribution of train/test dataste per class
        x = list(test_count.columns)
        y1 =train_count.iloc[0].to_list()
        y2 = test_count.iloc[0].to_list()
        plt.figure(figsize=(12,7))
        c = '#7eb54e'
        c1 = '#0096FF'
        plt.bar(x, y1, color=c1)
        plt.bar(x, y2, bottom=y1, color=c)
        plt.xlabel("Emotions")
        plt.ylabel("Train & Test data")
        plt.legend(["Train", "Test"], loc='upper left')
        plt.title(DATASET_NAME)
        plt.savefig(MODEL_NAME + '_'+ DATASET_NAME +'/'+ 'distribution.png')
        #plt.show()

def test_graphs_info(history, MODEL_NAME, DATASET_NAME):
    print('\n\nModel Scores\n')

    hs=history
    acc = hs['accuracy']
    val_acc = hs['val_accuracy']
    loss =  hs['loss']
    val_loss = hs['val_loss']
    auc =  hs['auc']
    val_auc = hs['val_auc']
    precision =hs['precision']
    val_precision =hs['val_precision']
    f1 = hs['f1_score']
    val_f1 = hs['val_f1_score']  

    fig, (ax1, ax2,ax3,ax4,ax5) = plt.subplots(1,5, figsize= (20,5))
    fig.suptitle(" MODEL'S METRICS VISUALIZATION ")

    ax1.plot(range(1, len(acc) + 1), acc)
    ax1.plot(range(1, len(val_acc) + 1), val_acc)
    ax1.set_title('History of Accuracy')
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Accuracy')
    ax1.legend(['training', 'validation'])


    ax2.plot(range(1, len(loss) + 1), loss)
    ax2.plot(range(1, len(val_loss) + 1), val_loss)
    ax2.set_title('History of Loss')
    ax2.set_xlabel('Epochs')
    ax2.set_ylabel('Loss')
    ax2.legend(['training', 'validation'])
    """
    ax3.plot(range(1, len(auc) + 1), auc)
    ax3.plot(range(1, len(val_auc) + 1), val_auc)
    ax3.set_title('History of AUC')
    ax3.set_xlabel('Epochs')
    ax3.set_ylabel('AUC')
    ax3.legend(['training', 'validation'])

    ax4.plot(range(1, len(precision) + 1), precision)
    ax4.plot(range(1, len(val_precision) + 1), val_precision)
    ax4.set_title('History of Precision')
    ax4.set_xlabel('Epochs')
    ax4.set_ylabel('Precision')
    ax4.legend(['training', 'validation'])

    ax5.plot(range(1, len(f1) + 1), f1)
    ax5.plot(range(1, len(val_f1) + 1), val_f1)
    ax5.set_title('History of F1-score')
    ax5.set_xlabel('Epochs')
    ax5.set_ylabel('F1 score')
    ax5.legend(['training', 'validation'])
    """
    plt.savefig(MODEL_NAME + '_'+ DATASET_NAME +'/'+ 'acc_val.png')

    plt.show()


def confusion_matrix_graphs(MODEL_NAME, DATASET_NAME, classes,cm, blue = False):


    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    fig, ax = plt.subplots(figsize=(8,6))
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)

    ax.figure.colorbar(im, ax=ax)

    ax.set(xticks=np.arange(cm.shape[1]),
        yticks=np.arange(cm.shape[0]),
        xticklabels=classes, yticklabels=classes,
        title = 'Normalized confusion matrix',
        ylabel='True label',
        xlabel='Predicted label')

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")


    fmt = '.2f' 
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")

    fig.tight_layout()
    plt.savefig(MODEL_NAME + '_'+ DATASET_NAME +'/'+  'conf_matrix1.png')

    #plt.show()
