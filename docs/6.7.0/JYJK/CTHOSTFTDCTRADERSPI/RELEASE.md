<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<p>非线程安全，多线程使用请加锁。</p>
<p>建议使用logout函数登出，等自动重连后再重新登录，以实现api实例重复使用。不建议直接release api实例。</p>
<span class="anchor" id="d2e193bd-bee6-4c7d-a9d7-7bcb7a5a40a7"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/RELEASE/">Release</a>() = 0;</p>
<span class="anchor" id="05271860-1ea0-4246-8da1-a6a12e8c7e12"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="7937e4ec-3a18-4713-bf1f-6cda2c900954"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8e9c61db-b376-410f-8b9e-11446d2bda8f"></span>
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
<span class="anchor" id="bf2cb88a-5605-4897-a654-5bd154676f9b"></span>
## 5.FAQ
<p>无</p>
