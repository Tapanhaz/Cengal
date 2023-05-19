// Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//     http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

# include <string.h>

extern void c_write_uint64(unsigned long long base_address, unsigned long long offset, unsigned long long value)
{
    unsigned long long* ptr = (unsigned long long*)(base_address + offset);
    *ptr = value;
}

extern unsigned long long c_read_uint64(unsigned long long base_address, unsigned long long offset)
{
    unsigned long long* ptr = (unsigned long long*)(base_address + offset);
    return *ptr;
}

extern void c_write_int64(unsigned long long base_address, unsigned long long offset, long long value)
{
    long long* ptr = (long long*)(base_address + offset);
    *ptr = value;
}

extern long long c_read_int64(unsigned long long base_address, unsigned long long offset)
{
    long long* ptr = (long long*)(base_address + offset);
    return *ptr;
}

extern void c_write_uint32(unsigned long long base_address, unsigned long long offset, unsigned int value)
{
    unsigned int* ptr = (unsigned int*)(base_address + offset);
    *ptr = value;
}

extern unsigned int c_read_uint32(unsigned long long base_address, unsigned long long offset)
{
    unsigned int* ptr = (unsigned int*)(base_address + offset);
    return *ptr;
}

extern void c_write_int32(unsigned long long base_address, unsigned long long offset, int value)
{
    int* ptr = (int*)(base_address + offset);
    *ptr = value;
}

extern int c_read_int32(unsigned long long base_address, unsigned long long offset)
{
    int* ptr = (int*)(base_address + offset);
    return *ptr;
}

extern void c_write_uint16(unsigned long long base_address, unsigned long long offset, unsigned short value)
{
    unsigned short* ptr = (unsigned short*)(base_address + offset);
    *ptr = value;
}

extern unsigned short c_read_uint16(unsigned long long base_address, unsigned long long offset)
{
    unsigned short* ptr = (unsigned short*)(base_address + offset);
    return *ptr;
}

extern void c_write_int16(unsigned long long base_address, unsigned long long offset, short value)
{
    short* ptr = (short*)(base_address + offset);
    *ptr = value;
}

extern short c_read_int16(unsigned long long base_address, unsigned long long offset)
{
    short* ptr = (short*)(base_address + offset);
    return *ptr;
}

extern void c_write_uint8(unsigned long long base_address, unsigned long long offset, unsigned char value)
{
    unsigned char* ptr = (unsigned char*)(base_address + offset);
    *ptr = value;
}

extern unsigned char c_read_uint8(unsigned long long base_address, unsigned long long offset)
{
    unsigned char* ptr = (unsigned char*)(base_address + offset);
    return *ptr;
}

extern void c_write_int8(unsigned long long base_address, unsigned long long offset, char value)
{
    char* ptr = (char*)(base_address + offset);
    *ptr = value;
}

extern char c_read_int8(unsigned long long base_address, unsigned long long offset)
{
    char* ptr = (char*)(base_address + offset);
    return *ptr;
}

extern void c_write_float(unsigned long long base_address, unsigned long long offset, float value)
{
    float* ptr = (float*)(base_address + offset);
    *ptr = value;
}

extern float c_read_float(unsigned long long base_address, unsigned long long offset)
{
    float* ptr = (float*)(base_address + offset);
    return *ptr;
}

extern void c_write_double(unsigned long long base_address, unsigned long long offset, double value)
{
    double* ptr = (double*)(base_address + offset);
    *ptr = value;
}

extern double c_read_double(unsigned long long base_address, unsigned long long offset)
{
    double* ptr = (double*)(base_address + offset);
    return *ptr;
}

extern void c_copy_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned long long source_offset)
{
    void* ptr = (unsigned long long*)(base_address + offset);
    void* source = (unsigned long long*)(base_address + source_offset);
    memcpy(ptr, source, (size_t)size);
}

extern void c_copy_memory_from(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned long long source_offset)
{
    void* ptr = (unsigned long long*)(base_address + offset);
    void* source = (unsigned long long*)(source_offset);
    memcpy(source, ptr, (size_t)size);
}

extern void c_set_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned char value)
{
    void* ptr = (unsigned long long*)(base_address + offset);
    memset(ptr, value, (size_t)size);
}

extern void c_zero_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size)
{
    void* ptr = (unsigned long long*)(base_address + offset);
    memset(ptr, 0, (size_t)size);
}
