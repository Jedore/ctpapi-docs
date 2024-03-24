<p>删除接口对象本身</p>
<p>不再使用本接口对象时,调用该函数删除接口对象</p>
<span class="anchor" id="85ccbb99-fc5a-48ed-9055-d771e95503ab"></span>
## 1.函数原型
<p>virtual void Release() = 0;</p>
<span class="anchor" id="fe55ff31-4610-4658-a64a-33a0fc16147e"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="1bd63577-45bc-4713-8f79-d58c55936708"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b3f8cdd1-1838-4a83-ad60-c2391fbc8ded"></span>
## 4.调用示例
<pre><code>template &lt;class TUserApi&gt;
void CUserApiEnv&lt;TUserApi&gt;::UnInitialUserApi()
{
    // 释放UserApi
    if (m_pUserApi)
    {
        m_pUserApi-&gt;RegisterSpi(NULL);
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
<span class="anchor" id="d89049a0-8dc3-4ba4-be73-7d672f54d47a"></span>
## 5.FAQ
<p>无</p>
