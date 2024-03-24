<p>用户口令更新请求响应，当执行ReqUserPasswordUpdate后，该方法被调用。</p>
<span class="anchor" id="153d81f0-8dd5-45cc-999d-c3e3ab84935b"></span>
## 1.函数原型
<p>virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0dea2e6d-fe3c-4fcf-84bf-44e1c7ff174f"></span>
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
<span class="anchor" id="dafbc47e-706a-49c7-aca4-0c79e63abd31"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="763964a5-b82c-47f2-99bf-d6e8db30b41b"></span>
## 4.FAQ
<p>无</p>
