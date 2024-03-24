<p>用户口令更新请求响应，当执行ReqUserPasswordUpdate后，该方法被调用。</p>
<span class="anchor" id="52dc2702-ce10-46bb-85a4-d5b4a098327c"></span>
## 1.函数原型
<p>virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="9e3d4d49-eaad-409c-90c4-ecc7981651dc"></span>
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
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="3bc36b0e-ba68-4457-90bd-06fc883a5006"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="36708ff6-2e8b-42b1-bea9-005ae607b53d"></span>
## 4.FAQ
<p>无</p>
