# Bill per hour
instance_bill = {'i4': 1,
                 'i5': 2,
                 'i6': 3,
                 'i7': 4
                 }
runtime = {'i4': 60,
           'i5': 30,
           'i6': 60,
           'i7': 30
           }

instance_count = {'i4': 1,
                  'i5': 1,
                  'i6': 1,
                  'i7': 1
                  }
# AWS provides 25% on all computing time and find the cost of overall run time.
discounted_cost = 0
total_cost = 0
for k,v in runtime.items():
    run_hr = v/60
    print(f'{k} runtime {run_hr} hrs and cost {instance_bill.get(k) * instance_count.get(k) * run_hr} and after 25% {(instance_bill.get(k) * instance_count.get(k) *  run_hr)*0.25}')
    total_cost += instance_bill.get(k) * instance_count.get(k) * run_hr
    discounted_cost += (instance_bill.get(k) * instance_count.get(k) * run_hr)*0.25
print(f'Total compute cost {total_cost}')
print(f'Total compute cost after 25%  {discounted_cost}')