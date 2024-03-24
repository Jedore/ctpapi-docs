<p>请求查询银期签约关系响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYACCOUNTREGISTER/">ReqQryAccountregister</a>后，该方法被调用</p>
<span class="anchor" id="88639f2c-2642-4100-b120-a9d2485a3060"></span>
## 1.函数原型
<p>virtual void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0a0f507e-d62d-41cd-842b-34f107b541c6"></span>
## 2.参数
<p>pAccountregister：客户开销户信息表</p>
<pre><code>struct CThostFtdcAccountregisterField
{
    ///交易日期
    TThostFtdcTradeDateType TradeDay;
    ///银行编码
    TThostFtdcBankIDType BankID;
    ///银行分支机构编码
    TThostFtdcBankBrchIDType BankBranchID;
    ///银行帐号
    TThostFtdcBankAccountType BankAccount;
    ///期货公司编码
    TThostFtdcBrokerIDType BrokerID;
    ///期货公司分支机构编码
    TThostFtdcFutureBranchIDType BrokerBranchID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///证件类型
    TThostFtdcIdCardTypeType IdCardType;
    ///证件号码
    TThostFtdcIdentifiedCardNoType IdentifiedCardNo;
    ///客户姓名
    TThostFtdcIndividualNameType CustomerName;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///开销户类别
    TThostFtdcOpenOrDestroyType OpenOrDestroy;
    ///签约日期
    TThostFtdcTradeDateType RegDate;
    ///解约日期
    TThostFtdcTradeDateType OutDate;
    ///交易ID
    TThostFtdcTIDType TID;
    ///客户类型
    TThostFtdcCustTypeType CustType;
    ///银行帐号类型
    TThostFtdcBankAccTypeType BankAccType;
    ///长客户姓名
    TThostFtdcLongIndividualNameType LongCustomerName;
};
</code></pre>
<p>BankID：银行编码</p>
<p>BankBranchID：值为0000</p>
<p>BrokerBranchID：值为0000</p>
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
<span class="anchor" id="1209274b-1891-49ca-95e4-11f2fef1ce71"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="68ffcd31-9ecc-4fd5-95dc-997c994abac7"></span>
## 4.FAQ
<p>无</p>
