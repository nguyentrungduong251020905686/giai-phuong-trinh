#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=1
b=2
c=3
print(a, b, c)
print(f"a={a}, b={b}, c={c}")


# In[30]:


if a==0:
    if b==0:      
        if c==0:  
            print("Phương trình có vô số nghiệm")
        else:  
            print("Phương trình vô nghiệm")
    else:  
        x=-c/b  
        print(f"Phương trình bậc nhất có nghiệm duy nhất:{x}")
else:
    x=-c/b
    print(f"Phương trình bậc nhất có nghiệm duy nhất{x}")


# In[41]:


delta=b**2-4*a*c
if delta>0: 
    x1=(-b+math.sqrt(delta))/(2*a)  
    x2=(-b-math.sqrt(delta))/(2*a)  
    print(f"Phương trình có hai nghiệm phân biệt: x1={x1}, x2={x2}")
elif delta==0:   
     x=-b/(2*a)
     print( f"Phương trình có nghiệm kép: x={x}")
else:
     print(f"phương trình vô nghiệm trong tập số thực.")
    


# In[ ]:





# In[ ]:




