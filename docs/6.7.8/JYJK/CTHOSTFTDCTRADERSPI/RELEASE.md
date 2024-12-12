<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<p>非线程安全，多线程使用请加锁。</p>
<p>建议使用logout函数登出，等自动重连后再重新登录，以实现api实例重复使用。不建议直接release api实例。</p>
<span class="anchor" id="dac47db5-fb31-433c-bef5-ff644dfa7936"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/RELEASE/">Release</a>() = 0;</p>
<span class="anchor" id="379a681b-01c9-47aa-a917-4d89d1c36065"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="26204d25-2b48-4770-ae7e-a6d2fdf23901"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1c1c1841-b815-42d6-b982-73ba7245972a"></span>
## 4.调用示例
<pre><code>template &lt;class TUserApi&gt;
void CUserApiEnv&lt;TUserApi&gt;::UnInitialUserApi()
{
    // 释放UserApi
    if (m_pUserApi)
    {
        m_pUserApi-&gt;Release();
        m_pUserApi = NULL;
    }
    // 释放UserSpi实例
    if (m_pUserSpiImpl)
    {
        delete m_pUserSpiImpl;
        m_pUserSpiImpl = NULL;
    }
}
</code></pre>
<span class="anchor" id="35f52d11-51a2-43a7-a093-f991c7b80b17"></span>
## 5.FAQ
<p>无</p>
