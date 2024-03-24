<p>用户口令更新请求，对应响应OnRspUserPasswordUpdate。</p>
<span class="anchor" id="d2e4085e-a535-4d3a-897d-7dec9f8513ae"></span>
## 1.函数原型
<p>virtual int ReqUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) = 0;</p>
<span class="anchor" id="70be0b1e-8f41-4b3c-8dd4-69f8d0aea93d"></span>
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
<span class="anchor" id="e40597aa-57a0-4b35-9d60-ff788cfceeb9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5e91eed8-9c61-431e-81e0-e5edf8f09701"></span>
## 4.调用示例
<pre><code>CThostFtdcUserPasswordUpdateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.UserID, "1000001");
strcpy_s(a.OldPassword, "123456");
strcpy_s(a.NewPassword, "666666");
m_pUserApi-&gt;ReqUserPasswordUpdate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="00487003-aed3-4d98-a24e-21db2d5b83be"></span>
## 5.FAQ
<p>无</p>
