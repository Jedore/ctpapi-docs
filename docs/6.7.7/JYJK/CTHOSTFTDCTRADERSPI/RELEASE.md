<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<p>非线程安全，多线程使用请加锁。</p>
<p>建议使用logout函数登出，等自动重连后再重新登录，以实现api实例重复使用。不建议直接release api实例。</p>
<span class="anchor" id="203f11fe-48a7-4eb5-983c-3f320b0f4747"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/RELEASE/">Release</a>() = 0;</p>
<span class="anchor" id="658f1bf4-28e8-485b-a367-0c4b588826ac"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="ae91f6dc-4c2c-431d-b717-eb0517d23b0a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="27bc7e51-4c7f-47ef-bcc9-fe56ed0571a3"></span>
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
<span class="anchor" id="b84bd5c7-1d00-4d14-a1f8-38a6fe12e534"></span>
## 5.FAQ
<p>无</p>
