<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<p>非线程安全，多线程使用请加锁。</p>
<p>建议使用logout函数登出，等自动重连后再重新登录，以实现api实例重复使用。不建议直接release api实例。</p>
<span class="anchor" id="4a576145-7f05-4d8a-b68f-f62669772464"></span>
## 1.函数原型
<p>virtual void Release() = 0;</p>
<span class="anchor" id="170195e4-9837-48c2-9870-4c98880ddbac"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="302ecb0e-b6d1-4336-9ad2-dff8b7c5057e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="51362e36-7dd0-469f-8074-04c9eaaf631c"></span>
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
<span class="anchor" id="d75d7773-fbe6-44b4-81e6-0844ad4f89de"></span>
## 5.FAQ
<p>无</p>
