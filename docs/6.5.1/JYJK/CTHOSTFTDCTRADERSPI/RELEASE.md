<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<p>非线程安全，多线程使用请加锁。</p>
<p>建议使用logout函数登出，等自动重连后再重新登录，以实现api实例重复使用。不建议直接release api实例。</p>
<span class="anchor" id="81b57f98-6249-486d-8bf4-8a5c657f557d"></span>
## 1.函数原型
<p>virtual void Release() = 0;</p>
<span class="anchor" id="5a811791-b49e-4a7e-b046-ccaffbd4dda8"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="696b3128-c7ee-4273-852e-e66e0a6e9b72"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b1ba5d00-1b4d-42bc-9ee8-985d0f131b8e"></span>
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
<span class="anchor" id="e715f39a-3f76-4319-808c-1f83470429ed"></span>
## 5.FAQ
<p>无</p>
