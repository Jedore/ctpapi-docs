<p>用户口令更新请求，对应响应OnRspUserPasswordUpdate。</p>
<span class="anchor" id="c5081fda-1790-44e0-8f12-915209a09720"></span>
## 1.函数原型
<p>virtual int ReqUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) = 0;</p>
<span class="anchor" id="3e3618de-dfd4-498a-8358-129c2e763f13"></span>
## 2.参数
<p>pUserPasswordUpdate：用户口令变更</p>
<pre><code>struct CThostFtdcUserPasswordUpdateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///原来的口令
    TThostFtdcPasswordType OldPassword;
    ///新的口令
    TThostFtdcPasswordType NewPassword;
};
</code></pre>
<p>NewPassword：新密码需要符合复杂度要求，不然修改失败。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="36330b14-5b6e-40f7-850b-b995aa8e8812"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7b43bdc9-b93d-4b78-851a-65eb83144b52"></span>
## 4.调用示例
<pre><code>CThostFtdcUserPasswordUpdateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.UserID, "1000001");
strcpy_s(a.OldPassword, "123456");
strcpy_s(a.NewPassword, "666666");
m_pUserApi-&gt;ReqUserPasswordUpdate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="06799bfa-6e76-4a7b-a2c7-7cbdd56476e4"></span>
## 5.FAQ
<p>无</p>
