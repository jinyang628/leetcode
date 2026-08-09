else if(ti>=tasks.size()){//ti ->task id
                //no servers are available and tasks to queue we forward time to just before next ongoing(earliest ending) task ends
                if(!times.empty()){ // times-> priority queue with ongoing tasks
                    int ttime = times.top()[0]; // time of earliest ending task
                    i=(ttime-1);//forwarded to just before earliest task end(it ends at next iteration)
                }
            }