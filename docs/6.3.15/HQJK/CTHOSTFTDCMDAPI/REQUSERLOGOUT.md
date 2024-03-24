<p>登出请求，对应响应OnRspUserLogout。</p>
<span class="anchor" id="499428f7-b810-40ff-9b37-ee4ffaebf1d0"></span>
## 1.函数原型
<p>virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;</p>
<span class="anchor" id="5f88d7b0-2d06-44dc-9486-c4e9390341d0"></span>
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
<span class="anchor" id="e48fe4bf-f8c5-4f26-b08e-49c8f7b9cd2b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6204809d-cb3e-4c7f-bccc-0f63b2d6208e"></span>
## 4.调用示例
<pre><code>CThostFtdcUserLogoutField a = { 0 };
m_pUserApi-&gt;ReqUserLogout(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="ec8dff37-ef53-4e1a-91f2-42c4a7f20794"></span>
## 5.FAQ
<p>无</p>
