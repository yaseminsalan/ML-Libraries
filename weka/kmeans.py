from subprocess import Popen, PIPE, STDOUT

# Settings to perform kmeans.
classpath = '~/weka.jar'
wekaFilter = 'weka.filters.unsupervised.attribute.AddCluster'
methode = 'weka.clusterers.SimpleKMeans -N 2'
inputFile = '../data/two_cluster.arff'

# Perform kmeans with 2 clusters.
p = Popen(['java', '-classpath', classpath,
			'weka.filters.unsupervised.attribute.AddCluster', 
			'-W', methode, '-i', inputFile],
			shell=False, bufsize=1, stdout=PIPE, stderr=STDOUT, close_fds=True)

# Show cluster association.
for line in iter(p.stdout.readline, b''):
    print line,
p.stdout.close()
p.wait()