<p>请求查询转帐银行响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRANSFERBANK/">ReqQryTransferBank</a>后，该方法被调用。</p>
<span class="anchor" id="6705bd59-6bbf-4753-a7db-676dea8aeb3e"></span>
## 1.函数原型
<p>virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="49fc06b4-10ef-47a0-a8a7-1ea902cdbdf3"></span>
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
<span class="anchor" id="e991d316-25f7-42df-bc18-7b181315e032"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="da49e72b-9b0a-4bb4-aeb6-6b2c8eafc990"></span>
## 4.FAQ
<p>无</p>
