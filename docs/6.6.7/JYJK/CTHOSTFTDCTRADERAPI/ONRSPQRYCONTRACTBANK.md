<p>请求查询签约银行响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCONTRACTBANK/">ReqQryContractBank</a>后，该方法被调用。</p>
<span class="anchor" id="030198dc-6727-47cd-a587-c980d102ac32"></span>
## 1.函数原型
<p>virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="da181421-21e0-4727-b3e7-402870519691"></span>
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
<span class="anchor" id="d4e6c5f0-16cd-48a7-80bb-f4ceab55922d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="eb0ccb7a-31f9-4189-bd8e-7b62e6bcdcb7"></span>
## 4.FAQ
<p>无</p>
