<p>请求查询转帐银行响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRANSFERBANK/">ReqQryTransferBank</a>后，该方法被调用。</p>
<span class="anchor" id="3e8d52fc-68e0-41c6-8f9e-4b2a6235c84d"></span>
## 1.函数原型
<p>virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d9a5981f-54d2-4baf-91f0-a52e4aeb5e64"></span>
## 2.参数
<p>pTransferBank：转帐银行</p>
<pre><code>struct CThostFtdcTransferBankField
{
    ///银行代码
    TThostFtdcBankIDType BankID;
    ///银行分中心代码
    TThostFtdcBankBrchIDType BankBrchID;
    ///银行名称
    TThostFtdcBankNameType BankName;
    ///是否活跃
    TThostFtdcBoolType IsActive;
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
<span class="anchor" id="a35c428d-430f-49e6-b7be-f31caf96cb3c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a2e18f20-80d2-4419-8ea7-10ee4924c068"></span>
## 4.FAQ
<p>无</p>
