<p>用户口令更新请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQUSERPASSWORDUPDATE/">ReqUserPasswordUpdate</a>后，该方法被调用。</p>
<span class="anchor" id="3b06b348-732a-414d-89c5-5f4171ab5334"></span>
## 1.函数原型
<p>virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="57542061-e0eb-4db8-86fc-796b24888cc5"></span>
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
<span class="anchor" id="24c0831e-a423-4585-bde0-6550bfff3308"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0ec56286-59b9-480e-b38f-3158d8b0f9c2"></span>
## 4.FAQ
<p>无</p>
