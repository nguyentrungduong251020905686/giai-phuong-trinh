#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter a positive integer:"))
print(n)


# In[2]:


s=0 #biến số dùng để lưu tổng
i=0 #số mở đầu 
while i<n:
    s+=i
    i+=2
print(f"The sum of 1 to {n} is {s}")


# In[ ]:




