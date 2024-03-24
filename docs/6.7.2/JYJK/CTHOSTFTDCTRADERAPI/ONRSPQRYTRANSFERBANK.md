<p>请求查询转帐银行响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRANSFERBANK/">ReqQryTransferBank</a>后，该方法被调用。</p>
<span class="anchor" id="e6fae49c-eb35-4951-9003-67cfdc5836e3"></span>
## 1.函数原型
<p>virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="36f4adba-9873-46b3-b551-a1d0aa900702"></span>
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
<span class="anchor" id="a6cca494-23b2-4eba-9c8b-382a07f0b335"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="561fb7ee-7b72-4020-8208-5e61dd8e4b44"></span>
## 4.FAQ
<p>无</p>
