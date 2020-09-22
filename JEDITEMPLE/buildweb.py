CREATE TABLE agents(
  agent_id VARCHAR(26) PRIMARY KEY,
  callback_id INTEGER NOT NULL,
  agent_name VARCHAR NOT NULL,
  os VARCHAR NULL,
  socket VARCHAR NOT NULL,
  status VARCHAR NULL 
);

CREATE TABLE agent_callback(
  id VARCHAR PRIMARY KEY,
  callback_id INTEGER NOT NULL,
  last_callback VARCHAR NOT NULL,
  next_callback VARCHAR NULL,
  callback_timer INTEGER NULL,
  FOREIGN KEY (callback_id) REFERENCES agents(callback_id)
);

CREATE TABLE agent_data(
  data_id INTEGER PRIMARY KEY,
  agent_id VARCHAR(26) NOT NULL,
  cmd_tasked VARCHAR NOT NULL,
  data_returned VARCHAR NULL,
  date_time TEXT NOT NULL,
  FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

CREATE TABLE agent_task(
  task_id INTEGER PRIMARY KEY,
  agent_id VARCHAR(26) NOT NULL,
  type VARCHAR NULL,
  value VARCHAR NULL,
  cmd VARCHAR NOT NULL,
  tasked_time TEXT NOT NULL,
  FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);
