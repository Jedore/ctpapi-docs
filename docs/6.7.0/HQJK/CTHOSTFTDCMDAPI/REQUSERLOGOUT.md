<p>登出请求，对应响应<a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPUSERLOGOUT/">OnRspUserLogout</a>。暂不支持。</p>
<span class="anchor" id="e2a9452d-5c7d-42f4-bf59-40389bfcdb5e"></span>
## 1.函数原型
<p>virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;</p>
<span class="anchor" id="478a8b57-1144-4229-b016-9cde4f65da19"></span>
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
<span class="anchor" id="dc114e51-79da-43bb-b479-83d8032352e3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6bba7e8f-0198-42ac-8e2d-8fcd2b11bab2"></span>
## 4.调用示例
<pre><code>CThostFtdcUserLogoutField a = { 0 };
m_pUserApi-&gt;ReqUserLogout(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="e86be3c3-f1f2-411c-b2a5-559ba8df0221"></span>
## 5.FAQ
<p>无</p>
