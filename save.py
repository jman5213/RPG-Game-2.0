import pickle

def load_info(load_to):
  load_file = open(load_to, "rb")
  to_return = pickle.load(load_file)
  load_file.close()
  return to_return

def save_info(save_to,data):
  load_file = open(save_to, "rb")
  pickle.dump(data,load_file)
  load_file.close()
  return