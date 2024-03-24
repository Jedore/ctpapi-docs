<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<p>非线程安全，多线程使用请加锁。</p>
<p>建议使用logout函数登出，等自动重连后再重新登录，以实现api实例重复使用。不建议直接release api实例。</p>
<span class="anchor" id="d639151a-2943-41bf-977a-7ca329b0c9a2"></span>
## 1.函数原型
<p>virtual void Release() = 0;</p>
<span class="anchor" id="668ef2b6-fdfa-425c-97af-4b193ce94d02"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="b4106048-9583-4561-86b9-f73893866530"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="cb87c5f4-7062-499d-923c-486120c50f75"></span>
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
<span class="anchor" id="511170e2-3b4d-4ca1-bb0a-7dbc851b6822"></span>
## 5.FAQ
<p>无</p>
