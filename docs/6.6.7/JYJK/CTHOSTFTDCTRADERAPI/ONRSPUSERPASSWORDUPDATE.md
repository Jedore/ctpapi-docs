<p>用户口令更新请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQUSERPASSWORDUPDATE/">ReqUserPasswordUpdate</a>后，该方法被调用。</p>
<span class="anchor" id="cbd8eed6-d511-402e-85f3-0beb5f0d5563"></span>
## 1.函数原型
<p>virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2f0b6089-18a0-4e72-89a0-2cb7103cfb35"></span>
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
<span class="anchor" id="14e771ff-f70c-445b-93b0-6bc7832a9d4f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1255be87-70e2-4d4c-a0da-05a204dc1257"></span>
## 4.FAQ
<p>无</p>
