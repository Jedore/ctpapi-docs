<p>请求查询转帐银行响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRANSFERBANK/">ReqQryTransferBank</a>后，该方法被调用。</p>
<span class="anchor" id="20d9b3f6-4816-49f5-8452-094f50b26975"></span>
## 1.函数原型
<p>virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="735053c5-bf5b-4265-a712-cf835d022397"></span>
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
<span class="anchor" id="31f46153-f76c-4879-a510-153e0e6e082f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c48674d6-50e0-4bfd-97fd-1546908d2492"></span>
## 4.FAQ
<p>无</p>
