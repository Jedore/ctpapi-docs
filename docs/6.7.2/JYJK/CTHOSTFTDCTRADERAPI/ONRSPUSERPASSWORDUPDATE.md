<p>用户口令更新请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQUSERPASSWORDUPDATE/">ReqUserPasswordUpdate</a>后，该方法被调用。</p>
<span class="anchor" id="aeaa6663-91cf-4439-b00b-0b1ac25fa0ec"></span>
## 1.函数原型
<p>virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="891d4622-9051-477a-a3bd-d333a329961b"></span>
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
<span class="anchor" id="b2e8e2d8-7f5d-4b9f-8bcd-11751f73a960"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f13db40b-7cb7-4173-aff8-1d7061de0f1e"></span>
## 4.FAQ
<p>无</p>
