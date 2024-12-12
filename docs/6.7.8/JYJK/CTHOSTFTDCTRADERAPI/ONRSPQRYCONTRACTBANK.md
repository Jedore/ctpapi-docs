<p>请求查询签约银行响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCONTRACTBANK/">ReqQryContractBank</a>后，该方法被调用。</p>
<span class="anchor" id="9ac59507-130b-46fe-9c61-05a17cf9ef95"></span>
## 1.函数原型
<p>virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3e673733-9524-42a4-9ec8-05863c6f421f"></span>
## 2.参数
<p>pContractBank：查询签约银行响应</p>
<pre><code>struct CThostFtdcContractBankField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///银行代码
    TThostFtdcBankIDType BankID;
    ///银行分中心代码
    TThostFtdcBankBrchIDType BankBrchID;
    ///银行名称
    TThostFtdcBankNameType BankName;
};
</code></pre>
<p>BankID：对应期货公司内部设置的银行编码</p>
<p>BankName：对应期货公司内部设置的银行名称</p>
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
<span class="anchor" id="4346b4f7-2232-490d-9cea-2a8b9a94cf4b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2c0aebb3-8711-4714-9612-36ebe9e57b70"></span>
## 4.FAQ
<p>无</p>
