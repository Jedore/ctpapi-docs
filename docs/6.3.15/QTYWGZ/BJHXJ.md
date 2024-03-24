<span class="anchor" id="a5672e65-edce-4e87-8791-1e1aadf7212d"></span>
## 1.指令介绍
<ul>
<li>1.请求询价指令</li>
</ul>
<p>发起询价指令使用ReqForQuoteInsert函数。</p>
<p>参数CThostFtdcInputForQuoteField中，ForQuoteRef非必填，可由CTP交易核心自动生成。</p>
<p>交易所有询价价差的限制，期货公司可以在柜台上进行设置，一般如下</p>
<table><tr><th style="TEXT-ALIGN: center;">经纪公司代码</th><th style="TEXT-ALIGN: center;">合约代码</th><th style="TEXT-ALIGN: center;">交易所代码</th><th style="TEXT-ALIGN: center;">最新价</th><th style="TEXT-ALIGN: center;">价差</th></tr><tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">0</td>
<td style="TEXT-ALIGN: left;">8</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">50</td>
<td style="TEXT-ALIGN: left;">10</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">100</td>
<td style="TEXT-ALIGN: left;">20</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">200</td>
<td style="TEXT-ALIGN: left;">30</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">300</td>
<td style="TEXT-ALIGN: left;">50</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">500</td>
<td style="TEXT-ALIGN: left;">75</td>
</tr>
</table>
<p>询价价差的判断过程</p>
<p>1)  看最新价对应于上面的哪一档次，确定价差的最小值</p>
<p>2)  计算买价和卖价的价差，看是否大于设置的价差（等于也不行）</p>
<p>3)  如果2)通过，那么询价单报入交易所，否则会被CTP直接拒绝。</p>
<p>如果询价的时候，当前合约价差不在范围，则报“CTP：当前价差禁止询价”。</p>
<p>另外，交易所还有询价时间间隔限制，一般在交易所端有控制，但郑商所控制在CTP柜台端，柜台设置例如：</p>
<img alt="" src="data:image/jpeg;base64,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"/>
<p>对于郑商所，如果询价过于频繁，则会报“CTP：当前时间禁止询价”。其他交易所报错类似。</p>
<ul>
<li>2.接收询价响应</li>
</ul>
<p>询价响应有以下几种：</p>
<table><tr><th style="TEXT-ALIGN: center;">函数名称</th><th style="TEXT-ALIGN: center;">说明</th></tr><tr><td style="TEXT-ALIGN: left;">OnRspForQuoteInsert</td>
<td style="TEXT-ALIGN: left;">只在录入错误的情况下返回，如字段校验失败、被限制询价等；可以通过ErrorID和ErrorMsg查看错误信息</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">OnRtnForQuoteRsp（交易spi）</td>
<td style="TEXT-ALIGN: left;"><font color="#FF0000">暂时不用</font></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">OnRtnForQuoteRsp（行情spi）</td>
<td style="TEXT-ALIGN: left;">录入成功后会推送，但是事先要调用行情api里的SubscribeForQuoteRsp去订阅该消息。</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">OnErrRtnForQuoteInsert</td>
<td style="TEXT-ALIGN: left;">被交易所拒绝的询价，通过此接口返回；可以通过ErrorID和ErrorMsg查看错误信息</td>
</tr>
</table>
<ul>
<li>3.查询询价</li>
</ul>
<p>查询询价使用ReqQryForQuote函数。</p>
<p>接收查询结果使用OnRspQryForQuote函数</p>
<ul>
<li>4.请求报价指令</li>
</ul>
<p>请求报价指令使用ReqQuoteInsert函数。</p>
<p>参数CThostFtdcInputQuoteField中，QuoteRef、AskOrderRef、BidOrderRef非必填，如果手工填则要求AskOrderRef<font color="#FF0000">小于</font>BidOrderRef，否则会报“CTP：重复的报单”。</p>
<ul>
<li>5.接收报价响应</li>
</ul>
<p>报价响应有以下几种：</p>
<table><tr><th style="TEXT-ALIGN: center;">函数名称</th><th style="TEXT-ALIGN: center;">说明</th></tr><tr><td style="TEXT-ALIGN: left;">OnRspQuoteInsert</td>
<td style="TEXT-ALIGN: left;">只在录入错误的情况下返回，如字段校验失败、无做市商权限等；可以通过ErrorID和ErrorMsg查看错误信息</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">OnRtnQuote</td>
<td style="TEXT-ALIGN: left;">当报价录入成功后，CTP给出该报价响应</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">OnRtnOrder</td>
<td style="TEXT-ALIGN: left;">报价录入成功后，如果是双边报价，CTP还会同时衍生出买卖两笔报价衍生单报入交易所，并返回相应的OnRtnOrder</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">OnRtnTrade</td>
<td style="TEXT-ALIGN: left;">衍生单成交后，返回该成交回报</td>
</tr>
</table>
<p>对于大商所，交易所在接受报价后，将不再维护报价状态的更新，所以客户端在接收CTP的报价回报时，<font color="#FF0000">其报价状态没有完整生命周期</font>。   详见<a href="../DJHDGZ/">报价回调规则</a></p>
<ul>
<li>6.撤销报价请求</li>
</ul>
<p>撤销报价请求使用ReqQuoteAction函数。</p>
<p>参数CThostFtdcInputQuoteActionField中，使用QuoteRef+SessionID+FrontID组合来撤单。</p>
<ul>
<li>7.撤销报价衍生单</li>
</ul>
<p>撤销报价衍生单使用ReqOrderAction函数。</p>
<p>参数CThostFtdcInputOrderActionField中，使用FrontID+SessionID+OrderRef组合来撤单。</p>
<p>要注意的是，如果在报价的时候没有填写AskOrderRef和BidOrderRef，那么报价衍生单的响应OnRtnOrder里的FrontID和SessionID是0。</p>
<ul>
<li>8.查询报价</li>
</ul>
<p>查询报价使用ReqQryQuote函数。</p>
<p>接收查询结果使用OnRspQryQuote函数</p>
<span class="anchor" id="e611fd47-b89b-4ffc-a2bb-63d79a2a7610"></span>
## 2.四所区别
<p>下面列出四所在询价和报价上的一些区别。<strong>注意：以下内容仅供参考，如果交易所的规则发生变化，文档并不会实时更新。</strong></p>
<ul>
<li>1.四所询价对比</li>
</ul>
<table><tr><th style="TEXT-ALIGN: center;">　</th><th style="TEXT-ALIGN: center;">中金所</th><th style="TEXT-ALIGN: center;">大商所</th><th style="TEXT-ALIGN: center;">郑商所</th><th style="TEXT-ALIGN: center;">上期所</th></tr><tr><td style="TEXT-ALIGN: center;">询价间隔如何设置</td>
<td style="TEXT-ALIGN: center;">交易所限制</td>
<td style="TEXT-ALIGN: center;">交易所限制</td>
<td style="TEXT-ALIGN: center;">CTP柜台</td>
<td style="TEXT-ALIGN: center;">交易所限制</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">普通投资者是否可接收询价申报</td>
<td style="TEXT-ALIGN: center;">可以</td>
<td style="TEXT-ALIGN: center;">可以</td>
<td style="TEXT-ALIGN: center;">可以</td>
<td style="TEXT-ALIGN: center;">可以</td>
</tr>
</table>
<ul>
<li>2.四所报价对比</li>
</ul>
<table><tr><th style="TEXT-ALIGN: center;">　</th><th style="TEXT-ALIGN: center;">中金所</th><th style="TEXT-ALIGN: center;">大商所</th><th style="TEXT-ALIGN: center;">郑商所</th><th style="TEXT-ALIGN: center;">上期所</th></tr><tr><td style="TEXT-ALIGN: center;">是否支持平仓</td>
<td style="TEXT-ALIGN: center;">支持</td>
<td style="TEXT-ALIGN: center;">支持</td>
<td style="TEXT-ALIGN: center;">支持</td>
<td style="TEXT-ALIGN: center;">支持</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">是否必须关联询价</td>
<td style="TEXT-ALIGN: center;">询价通知没有询价编号，不用填</td>
<td style="TEXT-ALIGN: center;">询价通知有编号，但是非必填，如做市商要完成义务率则要填</td>
<td style="TEXT-ALIGN: center;">询价通知有编号，但是非必填，如做市商要完成义务率则要填</td>
<td style="TEXT-ALIGN: center;">询价通知没有询价编号，不用填</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">是否支持单边报价</td>
<td style="TEXT-ALIGN: center;">不支持，提示“CTP:报单字段有误”</td>
<td style="TEXT-ALIGN: center;">支持，数量填0</td>
<td style="TEXT-ALIGN: center;">不支持，提示“CTP:报单字段有误”</td>
<td style="TEXT-ALIGN: center;">不支持，提示“CTP:报单字段有误”</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">是否支持市价单</td>
<td style="TEXT-ALIGN: center;">不支持，交易所提示：“已撤单报单被拒绝CFFEX:价格跌破跌停板”</td>
<td style="TEXT-ALIGN: center;">不支持，交易所提示：已撤单报单被拒绝DCE:期权价格必须大于等于TICK!</td>
<td style="TEXT-ALIGN: center;">不支持，交易所提示：“已撤单报单被拒绝CZCE:出错: 限价单价格不能为0或负数”</td>
<td style="TEXT-ALIGN: center;">不支持</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">双边报价买卖数量可否不一致</td>
<td style="TEXT-ALIGN: center;">可以不一致</td>
<td style="TEXT-ALIGN: center;">可以不一致</td>
<td style="TEXT-ALIGN: center;">CTP:不可以，提示“CTP：报单字段有误”</td>
<td style="TEXT-ALIGN: center;">CTP:不可以，提示“CTP：报单字段有误”</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">双边报价卖价是否必须大于买价</td>
<td style="TEXT-ALIGN: center;">一定是低价买，高价卖。否则会形成自成交</td>
<td style="TEXT-ALIGN: center;">必须，否则交易所提示： 已撤单报单被拒绝DCE:双边报价指令卖价必须大于买价</td>
<td style="TEXT-ALIGN: center;">必须，否则交易所提示：已撤单报单被拒绝CZCE: 出错：卖价(40800)必需大于买价(94800)</td>
<td style="TEXT-ALIGN: center;">一定是低价买，高价卖。否则会形成自成交</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">是否支持套保属性</td>
<td style="TEXT-ALIGN: center;">支持</td>
<td style="TEXT-ALIGN: center;">不支持，提示“CTP:该期权合约只支持投机类型报单”</td>
<td style="TEXT-ALIGN: center;">不支持，提示“CTP：该期权合约只支持投机类型报单”</td>
<td style="TEXT-ALIGN: center;">支持</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">是否会撤销前一次报价</td>
<td style="TEXT-ALIGN: center;">不会撤销</td>
<td style="TEXT-ALIGN: center;">不会撤销</td>
<td style="TEXT-ALIGN: center;">会撤销</td>
<td style="TEXT-ALIGN: center;">会撤销</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">是否支持撤单腿</td>
<td style="TEXT-ALIGN: center;">可以</td>
<td style="TEXT-ALIGN: center;">可以</td>
<td style="TEXT-ALIGN: center;">不可以</td>
<td style="TEXT-ALIGN: center;">不可以</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">双边报价开平可否不一致</td>
<td style="TEXT-ALIGN: center;">可以</td>
<td style="TEXT-ALIGN: center;">可以</td>
<td style="TEXT-ALIGN: center;">可以</td>
<td style="TEXT-ALIGN: center;">可以</td>
</tr>
</table>
