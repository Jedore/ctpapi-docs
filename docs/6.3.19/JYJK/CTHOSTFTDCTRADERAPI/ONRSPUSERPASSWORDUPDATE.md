<p>用户口令更新请求响应，当执行ReqUserPasswordUpdate后，该方法被调用。</p>
<span class="anchor" id="c0e85a15-ffe9-47e3-b0b8-268565c84606"></span>
## 1.函数原型
<p>virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="fe2ec28c-8b85-4787-9e1a-499f24ef2162"></span>
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
<span class="anchor" id="2c19e666-6694-42c7-a4dd-a70aa06ebb82"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8f7074d3-550c-4e05-accf-2e27b6addf6c"></span>
## 4.FAQ
<p>无</p>
