<p>登出请求，对应响应<a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPUSERLOGOUT/">OnRspUserLogout</a>。暂不支持。</p>
<span class="anchor" id="47d552b9-6062-4a19-9f72-4d5fb8b674b4"></span>
## 1.函数原型
<p>virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;</p>
<span class="anchor" id="c8ff0da9-65dc-4957-afd7-158b6a70236a"></span>
## 2.参数
<p>pUserLogout：用户登出请求</p>
<pre><code>struct CThostFtdcUserLogoutField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="2ff298ce-31d7-43d4-b508-c2127ae8f160"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ddc6b134-3f8d-4b2b-8bdc-407afe4de80d"></span>
## 4.调用示例
<pre><code>CThostFtdcUserLogoutField a = { 0 };
m_pUserApi-&gt;ReqUserLogout(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="5b49e54d-ce62-46b1-af58-d159ab18be0f"></span>
## 5.FAQ
<p>无</p>
