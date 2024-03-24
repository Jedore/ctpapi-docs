<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<p>非线程安全，多线程使用请加锁。</p>
<p>建议使用logout函数登出，等自动重连后再重新登录，以实现api实例重复使用。不建议直接release api实例。</p>
<span class="anchor" id="ad4f9db1-370a-4cd5-8900-b6d0dbb00e07"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/RELEASE/">Release</a>() = 0;</p>
<span class="anchor" id="d72fccbe-66f8-4399-b322-a1d39a97ced1"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="f43c5f15-63be-4e7d-8e0d-66c1314aa918"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ea8ce807-36ed-4d29-83b9-062db9ce7270"></span>
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
<span class="anchor" id="c54fb467-8429-42e5-ba4f-e467f7146a9b"></span>
## 5.FAQ
<p>无</p>
