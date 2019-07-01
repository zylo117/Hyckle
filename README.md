**Hyckle is a high-level warpper of pickle that provides data serialization for all python-pickleable object with the support of local read & write, better compression (approximately 50%-60% filesize smaller than original pickle @ default) and more memory-friendly.**

**Hyckle是pickle的一个高层封装，可以为所有可pickle的python变量提供数据序列化，同时支持局部读写，拥有更好的压缩率（文件大小在默认模式下比原生pickle小了约50%-60%）,并更节省内存。**

---

**Installation**

    pip install hyckle

---
**Demo:**

**Basic Usage**

    # create or reload a hyckle file. 
    # This will create a new hyckle file if not exists or reload a existed hyckle file.
    hk = Hyckle('helloworld.hyckle')
    
    # use hyckle as a dict
    hk.add('test_0', any_pickleable_object_0)
    hk.add('test_1',any_pickleable_object_1)
    hk.add('test_2',any_pickleable_object_2)
    hk.add('test_3',any_pickleable_object_3)
    
    # use hyckle as a list
    hk.append(any_pickleable_object_4)
    hk.append(any_pickleable_object_5)
    
    # check the length of hyckle
    length = len(hk)
    
    # use hyckle as a iterable object
    for obj in hk:
        do_something(obj)
    
    # get certain object by key: str
    obj_0 = hk.get(key)
    # or using getitem method
    obj_1 = hk[key]
    
    # get certain object by index: int
    obj_2 = hk[index]
    
    # get certain items by slice
    objs = hk[233:666]
    
    # remove key in hyckle
    hk.remove('test_0')
    
    # flush to disk. 
    # Normally hyckle will auto-flush to disk every K item adding (K = buffersize)
    hk.flush()
    
    # close a hyckle file. 
    # After final reading/writing hyckle, you should close it to ensure data integrity.
    hk.close()

**Advanced Usage**:

    # create a hyckle with custom compression,
    # lzma is much slower but smaller
    hk = Hyckle('helloworld.hyckle', compression='lzma')
    
    # or use gzip (default) with different compression level,
    # bigger number means smaller filesize.
    hk = Hyckle('helloworld.hyckle', compression=9)
    
    # sppedup I/O using bigger buffer.
    # Noted, bigger buffersize means allocating more memory.
    hk = Hyckle('helloworld.hyckle', buffer_size=128)
