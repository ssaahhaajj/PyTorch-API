from thop import profile as pf_flop
import torchprof as pf_time
import pandas as DataFrame

def profile(model, inp_data, want_op_file=False, cuda_=False):
  df1 = pf_flop(model, inputs=(inp_data, ))  
  with pf_time.Profile(model, use_cuda=cuda_) as prof:
    model(inp_data)
  df2=prof.display()
  mynn={"Layer Name":[],"FLOPs":[],"Self CPU total":[], "CPU Total":[], "GPU Total":[],"Input Features":[], "Output Features":[], "Dict Size of Emb":[], "Emb Vector Size":[], "Norm Size":[]}
  for i1 in df1.index:
    mynn["Layer Name"].append(df2["Layer Name"][i1])
    mynn["Self CPU total"].append(df2["Self CPU total"][i1])
    mynn["CPU Total"].append(df2["CPU total"][i1])
    mynn["GPU Total"].append(df2["GPU total"][i1])
    mynn["Input Features"].append(df1["Input Features"][i1])
    mynn["Output Features"].append(df1["Output Features"][i1])
    mynn["Dict Size of Emb"].append(df1["Dict Size of Emb"][i1])
    mynn["Emb Vector Size"].append(df1["Emb Vector Size"][i1])
    mynn["Norm Size"].append(df1["Norm Size"][i1])
  df3=DataFrame(mynn, columns= ["Layer Name","FLOPs","Self CPU total","CPU Total","GPU Total","Input Features","Output Features","Dict Size of Emb","Emb Vector Size","Norm Size"])
  if want_op_file==True:
    export_csv = df3.to_csv (r'output_file.csv', index = None, header=True)
  else:
    print(df3)
    
    
