<p>登出请求，对应响应<a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPUSERLOGOUT/">OnRspUserLogout</a>。暂不支持。</p>
<span class="anchor" id="ccd88f32-e5c0-4321-a81e-1d2006c1bef9"></span>
## 1.函数原型
<p>virtual int <a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REQUSERLOGOUT/">ReqUserLogout</a>(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;</p>
<span class="anchor" id="07deaa64-b823-486d-af71-5923c1e51c4a"></span>
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
<span class="anchor" id="97b8c957-0657-4595-a955-d650fee070e1"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="e3eaac03-2443-4c17-a2f2-c32f411a1133"></span>
## 4.调用示例
<pre><code>CThostFtdcUserLogoutField a = { 0 };
m_pUserApi-&gt;ReqUserLogout(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="a485458d-ef9e-4b07-97c2-330ed9aab6f4"></span>
## 5.FAQ
<p>无</p>
