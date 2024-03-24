<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<p>非线程安全，多线程使用请加锁。</p>
<p>建议使用logout函数登出，等自动重连后再重新登录，以实现api实例重复使用。不建议直接release api实例。</p>
<span class="anchor" id="c1ac9f0f-89d7-476d-895c-5008b6cd0d68"></span>
## 1.函数原型
<p>virtual void Release() = 0;</p>
<span class="anchor" id="46b1fbef-d86a-485f-bf29-8eac16ae089e"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="d6efcd4f-027d-4ae9-b229-75cd4b435149"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1ebd5128-3e22-41db-be42-9c936be8ed12"></span>
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
<span class="anchor" id="c0a76188-451c-4d47-ab6f-1226ed5b753b"></span>
## 5.FAQ
<p>无</p>
