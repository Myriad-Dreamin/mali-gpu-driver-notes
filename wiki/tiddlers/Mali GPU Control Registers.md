## GPU General Control Registers

### Read Only Registers

+ `GPU_ID`

+ `*_FEATURES`

  + `L2`: Level 2 cache features

  + `TILER`: Tiler features

  + `MEM`: Memory system features

  + `MMU`: MMU features

+ `GPU_IRQ_STATUS`

+ `GPU_STATUS`

+ `GPU_FAULTSTATUS`

+ `GPU_FAULTADDRESS(LO, HI)`

+ `GPU_FAULTSTATUS`

+ `CYCLE_COUNT(LO, HI)`

+ `TIMESTAMP(LO, HI)`

+ `THREAD_MAX_THREADS`

+ `THREAD_MAX_WORKGROUP_SIZE`

+ `THREAD_MAX_BARRIER_SIZE`

+ `THREAD_FEATURES`

+ `THREAD_TLS_ALLOC`

+ `TEXTURE_FEATURES(n)`

+ `SHADER_PRESENT_LO`

+ `TILER_PRESENT_LO`

+ `L2_PRESENT_LO`

+ `STACK_PRESENT_LO`

+ `SHADER_READY_LO`

+ `TILER_READY_LO`

+ `L2_READY_LO`

+ `TILER_READY_LO`

+ `STACK_READY_LO`

+ `STACK_PWRON_LO`

+ `STACK_PWROFF_LO`

+ `SHADER_PWRTRANS_LO`

+ `TILER_PWRTRANS_LO`

+ `L2_PWRTRANS_LO`

+ `STACK_PWRTRANS_LO`

+ `SHADER_PWRACTIVE_LO`

+ `TILER_PWRACTIVE_LO`

+ `L2_PWRACTIVE_LO`

+ `COHERENCY_FEATURES`

+ `L2_PWRON_LO`

+ `L2_PWRON_LO`


### Write Only Registers

+ `GPU_IRQ_CLEAR`

+ `GPU_COMMAND`

+ `PWR_KEY`

+ `PWR_OVERRIDE0`

+ `PWR_KEY`

+ `PWR_KEY`

+ `SHADER_PWRON_LO`

+ `TILER_PWRON_LO`

+ `L2_PWRON_LO`

+ `SHADER_PWROFF_LO`

+ `TILER_PWROFF_LO`

+ `L2_PWROFF_LO`

+ `L2_PWRON_LO`

+ `L2_PWRON_LO`

+ `L2_PWRON_LO`

+ `L2_PWRON_LO`

+ `L2_PWRON_LO`


### Read-Write Registers

+ `GPU_IRQ_RAWSTAT`

+ `GPU_IRQ_MASK`

+ `L2_CONFIG`

+ `PWR_OVERRIDE0`

+ `PWR_OVERRIDE1`

+ `COHERENCY_ENABLE`

+ `SHADER_CONFIG`

+ `TILER_CONFIG`

+ `L2_MMU_CONFIG`

+ `JOB_*`: Job control registers

+ `MMU_*`: MMU control registers

+ `AS_*`: MMU address space control registers



## Job Manage Registers

### Read Only Registers
+ `CORE_FEATURES`: Shader Core Features
+ `JS_PRESENT`: Job slots present
+ `LATEST_FLUSH`: Flush ID of latest clean-and-invalidate operation
+ `JS_FEATURES_REG(n)`: Features of job slot $n$ ($0 \leqslant n < 2^4$)

  + values: `NULL_JOB`, `SET_VALUE_JOB`, `CACHE_FLUSH_JOB`, `COMPUTE_JOB`, `VERTEX_JOB`, `GEOMETRY_JOB`, `TILER_JOB`, `FUSED_JOB`, `FRAGMENT_JOB`

+ `JS_HEAD(LO, HI)`: Job queue head pointer for job slot $n$

+ `JS_TAIL(LO, HI)`: Job queue tail pointer for job slot $n$

+ `JS_AFFINITY(LO, HI)`: Core affinity mask for job slot $n$

+ `JS_XAFFINITY`

### Write Only Registers

+ `JS_COMMAND`

  + values: `NOP`, `START`, `SOFT_STOP`, `HARD_STOP`, `SOFT_STOP_0`, `HARD_STOP_0`, `SOFT_STOP_1`, `HARD_STOP_1`
  + mask: 0x07

### Read-Write Registers
+ `PRFCNT`: Performance counter related control registers

   + `BASE_LO`/`BASE_HI`: memory region base address, low/high word

+ `JM_CONFIG`: Job manager configuration (implementation-specific)

  + values: `TIMESTAMP_OVERRIDE`, `CLOCK_GATE_OVERRIDE`, `JOB_THROTTLE_ENABLE`, `JOB_THROTTLE_LIMIT_SHIFT`, `MAX_JOB_THROTTLE_LIMIT`, `FORCE_COHERENCY_FEATURES_SHIFT`
+ `JOB_IRQ_JS_STATE`

+ `JOB_IRQ_THROTTLE`
+ `JOB_SLOT_REG(n, r)` the $r$-th register of job slot $n$ ($0 \leqslant n < 2^4, r < 32$?)
+ `JS_CONFIG`

  + values: `START_FLUSH_NO_ACTION`, `START_FLUSH_CLEAN`, `START_FLUSH_CLEAN_INVALIDATE`, `START_MMU`, `JOB_CHAIN_FLAG`, `END_FLUSH_NO_ACTION`, `END_FLUSH_CLEAN`, `END_FLUSH_CLEAN_INVALIDATE`, `ENABLE_FLUSH_REDUCTION`, `DISABLE_DESCRIPTOR_WR_BK`, `THREAD_PRI(n)`
+ `JS_STATUS`

  + values: 
    + Group of values representing the job status instead of a particular fault: `INTERRUPTED`, `STOPPED`, `TERMINATED`
    + General fault values: `CONFIG_FAULT`, `POWER_FAULT`, `READ_FAULT`, `WRITE_FAULT`, `AFFINITY_FAULT`, `BUS_FAULT`
    + Instruction or data faults: `INSTR_INVALID_PC`, `INSTR_INVALID_ENC`, `INSTR_TYPE_MISMATCH`, `INSTR_OPERAND_FAULT`, `INSTR_TLS_FAULT`, `INSTR_BARRIER_FAULT`, `INSTR_ALIGN_FAULT`, `DATA_INVALID_FAULT`, `TILE_RANGE_FAULT`, `ADDRESS_RANGE_FAULT`
    + Other faults: `OUT_OF_MEMORY`, `UNKNOWN`
+ `JS_HEAD_NEXT`
+ `JS_AFFINITY_NEXT`
+ `JS_CONFIG_NEXT`
+ `JS_XAFFINITY_NEXT`
+ `JS_COMMAND_NEXT`
+ `JS_FLUSH_ID_NEXT`


### unknown values

+ `GPU_COMMAND`: NOP, SOFT_RESET, HARD_RESET, PRFCNT_CLEAR, PRFCNT_SAMPLE, CYCLE_COUNT_START, CYCLE_COUNT_STOP, CLEAN_CACHES, CLEAN_INV_CACHES, SET_PROTECTED_MODE
