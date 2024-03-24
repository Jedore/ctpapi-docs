<p>登出请求，对应响应OnRspUserLogout。</p>
<span class="anchor" id="cbe959e3-ec78-4740-8a62-85c114ada337"></span>
## 1.函数原型
<p>virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;</p>
<span class="anchor" id="dfca0f6f-7429-4f93-8037-262646162a71"></span>
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
<span class="anchor" id="1dca6ac0-7b3a-4b5b-9f86-c6d3a19caf28"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="38f22819-d317-4c73-af77-ea19dc3db00f"></span>
## 4.调用示例
<pre><code>CThostFtdcUserLogoutField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.UserID, "1000001");
m_pUserApi-&gt;ReqUserLogout(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="8a5635db-02aa-43df-a416-3582a3e5d4ae"></span>
## 5.FAQ
<p>无</p>
