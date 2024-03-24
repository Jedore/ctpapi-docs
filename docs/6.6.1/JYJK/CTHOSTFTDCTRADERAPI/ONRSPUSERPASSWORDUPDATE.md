<p>用户口令更新请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQUSERPASSWORDUPDATE/">ReqUserPasswordUpdate</a>后，该方法被调用。</p>
<span class="anchor" id="74383288-0d31-41ad-92d9-cff7313834d8"></span>
## 1.函数原型
<p>virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="9433f00d-97ea-40b1-a19a-157ee1c74c0f"></span>
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
<span class="anchor" id="ad4540c9-9aec-4ca1-9dce-1df097677547"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5a8cf625-9f30-493b-98f1-fc48596998d2"></span>
## 4.FAQ
<p>无</p>
