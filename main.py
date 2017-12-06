import threading
from queue import Queue
from spider import spider
from domain import *
from general import *



#we have to make the user to fill this
PROJECT_NAME = 'stack'
HOMEPAGE = 'https://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME +'/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 4
queue = Queue()
spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
#thread queue
#spider(project,page,domain)

#2 functions for threads/workers
#Do the next joib in the queue
def work():
	while True:
		url = queue.get()
		spider.crawl_page(threading.current_thread().name, url)
		queue.task_done()
# Create worker threads (will be destroyed when the main exits)
def create_workers():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		#daemon process making it destroyed when it stop
		t.daemon = True
		t.start()

#2 functions for creating jobs
#Each queue link is a new job
def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()

# check if there are items in the queue if so crawl them

def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links) > 0 :
		print(str(len(queued_links)) + "links in the queue")
		create_jobs()



create_workers()
crawl()