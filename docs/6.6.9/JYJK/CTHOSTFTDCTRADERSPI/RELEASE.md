<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<p>非线程安全，多线程使用请加锁。</p>
<p>建议使用logout函数登出，等自动重连后再重新登录，以实现api实例重复使用。不建议直接release api实例。</p>
<span class="anchor" id="a1449ed0-eca5-4ec7-a671-89830caad781"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/RELEASE/">Release</a>() = 0;</p>
<span class="anchor" id="f71403f4-93f9-4ca9-87e0-8a699627af34"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="cc839ab6-7dc8-4792-a4f1-8ed18ce5937b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="240b65de-1863-4a2f-8d64-1799f615ee33"></span>
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
<span class="anchor" id="845dd577-f03b-415f-b71b-7966fb0437f1"></span>
## 5.FAQ
<p>无</p>
