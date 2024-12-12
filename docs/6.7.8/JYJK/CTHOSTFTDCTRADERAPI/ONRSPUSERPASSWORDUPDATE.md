<p>用户口令更新请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQUSERPASSWORDUPDATE/">ReqUserPasswordUpdate</a>后，该方法被调用。</p>
<span class="anchor" id="d2f4206f-3a5a-4e14-b548-878d2ecf004f"></span>
## 1.函数原型
<p>virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="56332aec-cb99-46f6-b9cc-a67cfeee5ea4"></span>
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
<span class="anchor" id="81e81e9e-97b8-42fe-9bae-95be99943a20"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4503b55b-9401-46f1-89a6-1c0b8347047c"></span>
## 4.FAQ
<p>无</p>
