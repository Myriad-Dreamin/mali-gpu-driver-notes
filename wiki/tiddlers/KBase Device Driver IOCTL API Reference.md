当File处于set up阶段时，只有以下两个api可用：

### kbase_api_handshake

协商API版本，major以kernel中的值为主，否则minor取两者较小值。

从该API可以看出，每个以file生命周期为参考的session都有独立的`kbase_context`。

INOUT参数：

```c
/**
 * struct kbase_ioctl_version_check - Check version compatibility with kernel
 *
 * @major: Major version number
 * @minor: Minor version number
 */
struct kbase_ioctl_version_check {
	__u16 major;
	__u16 minor;
};
```

### kbase_api_set_flags

协商api特性参数。

```c
/**
 * struct kbase_ioctl_set_flags - Set kernel context creation flags
 *
 * @create_flags: Flags - see base_context_create_flags
 */
struct kbase_ioctl_set_flags {
	__u32 create_flags;
};
```

`create_flags`类型实际为下面说明：

```c
/**
 * typedef base_context_create_flags - Flags to pass to ::base_context_init.
 *
 * Flags can be ORed together to enable multiple things.
 *
 * These share the same space as BASEP_CONTEXT_FLAG_*, and so must
 * not collide with them.
 */
typedef u32 base_context_create_flags;
```

---

当`kbase_context`创建以后，就可以开始正常API的调用。API调用的功能包括：

+ 给GPU派发工作

+ 分配GPU内存

### kbase_api_job_submit

直接就调用了`kbase_jd_submit`, jd即Job Dispather的缩写。jd会将任务派发给js，即Job Scheduler，js会将任务交给jm，即Job Manager

入参如下：

```c
/**
 * struct kbase_ioctl_job_submit - Submit jobs/atoms to the kernel
 *
 * @addr: Memory address of an array of struct base_jd_atom_v2
 * @nr_atoms: Number of entries in the array
 * @stride: sizeof(struct base_jd_atom_v2)
 */
struct kbase_ioctl_job_submit {
	__u64 addr;
	__u32 nr_atoms;
	__u32 stride;
};
```

`kbase_jd_submit`的描述如下：

```c
/**
 * kbase_jd_submit - Submit atoms to the job dispatcher
 *
 * @kctx: The kbase context to submit to
 * @user_addr: The address in user space of the struct base_jd_atom_v2 array
 * @nr_atoms: The number of atoms in the array
 * @stride: sizeof(struct base_jd_atom_v2)
 * @uk6_atom: true if the atoms are legacy atoms (struct base_jd_atom_v2_uk6)
 *
 * Return: 0 on success or error code
 */
int kbase_jd_submit(struct kbase_context *kctx,
		void __user *user_addr, u32 nr_atoms, u32 stride,
		bool uk6_atom);
```

### kbase_api_mem_alloc

分配一块足够大的GPU内存，虚拟地址由GPU确定，大小按页对齐。内存管理的特性满足配置`base_mem_alloc_flags`。一旦分配，是否能够修改根据`BASEP_MEM_FLAGS_KERNEL_ONLY`确定，即使有这个也可以在内核态中修改。

```c
/**
 * union kbase_ioctl_mem_alloc - Allocate memory on the GPU
 *
 * @va_pages: The number of pages of virtual address space to reserve
 * @commit_pages: The number of physical pages to allocate
 * @extent: The number of extra pages to allocate on each GPU fault which grows
 *          the region
 * @flags: Flags
 * @gpu_va: The GPU virtual address which is allocated
 *
 * @in: Input parameters
 * @out: Output parameters
 */
union kbase_ioctl_mem_alloc {
	struct {
		__u64 va_pages;
		__u64 commit_pages;
		__u64 extent;
		__u64 flags;
	} in;
	struct {
		__u64 flags;
		__u64 gpu_va;
	} out;
};
```

> todo, mem flags analysis

```c
```